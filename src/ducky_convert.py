import os
import sys
sys.path.append('/app/QuantumDuck/quantumduck')
import argparse
import quantum

class DuckyConvert:
    DEFAULT_KEY = "ANY_KEY"

    def __init__(self, scripts_dir, target):
        self.scripts_dir = scripts_dir
        self.target = target

    def convert(self):
        converted = self.convert_scripts()
        self.write_enum_keycodes(converted)
        self.write_keymap(converted)
        self.write_scripts(converted)

    def convert_scripts(self):
        scripts = {}
        for layerdir in os.listdir(self.scripts_dir):
            layer_key = layerdir.upper()
            layerdir_path = os.path.join(self.scripts_dir, layerdir)
            for scriptfile in os.listdir(layerdir_path):
                scripts[layer_key] = {}
                if scriptfile.endswith(".txt"):
                    script_key = ".".join(scriptfile.split(".")[:-1]).upper()
                    script_path = os.path.join(self.scripts_dir, layerdir, scriptfile)
                    scripts[layer_key][script_key] = quantum.DuckScript.create_duckscript_object(script_path)
        return scripts

    def write_enum_keycodes(self, scripts_dict):
        with open(self.target, "w") as target_file: 
            target_file.write("enum custom_keycodes {\n")
            target_file.write("\t{},\n".format(self.DEFAULT_KEY))
            for layerkey in sorted(scripts_dict.keys()):
                for scriptskey in sorted(scripts_dict[layerkey].keys()):
                    target_file.write("\t{},\n".format(self.keycode(layerkey, scriptskey)))
            target_file.write("};\n")

    def write_keymap(self, scripts_dict):
        with open(self.target, "a") as target_file: 
            target_file.write("\nconst uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {\n")
            for layer_index, layerkey in enumerate(sorted(scripts_dict.keys())):
                keys = sorted(scripts_dict[layerkey].keys())[:8]
                num_of_scripts  = len(keys)
                target_file.write("\t[{}]  = LAYOUT(".format(layer_index))
                target_file.write("""
             {},             {},
       {},       {}, {},       {},
             {},             {}\n""".format(
                                  self.keycode(layerkey, keys[0]) if 0 < num_of_scripts else self.DEFAULT_KEY,
                                  self.keycode(layerkey, keys[1]) if 1 < num_of_scripts else self.DEFAULT_KEY,
                                  self.keycode(layerkey, keys[2]) if 2 < num_of_scripts else self.DEFAULT_KEY,
                                  self.keycode(layerkey, keys[3]) if 3 < num_of_scripts else self.DEFAULT_KEY,
                                  self.keycode(layerkey, keys[4]) if 4 < num_of_scripts else self.DEFAULT_KEY,
                                  self.keycode(layerkey, keys[5]) if 5 < num_of_scripts else self.DEFAULT_KEY,
                                  self.keycode(layerkey, keys[6]) if 6 < num_of_scripts else self.DEFAULT_KEY,
                                  self.keycode(layerkey, keys[7]) if 7 < num_of_scripts else self.DEFAULT_KEY
                              ))
                target_file.write("\t),\n")
            target_file.write("};\n")

    def write_scripts(self, scripts_dict):
        with open(self.target, "a") as target_file: 
            target_file.write("bool process_record_user(uint16_t keycode, keyrecord_t *record) {\n")
            target_file.write("\tswitch (keycode) {\n")
            self.write_key_case(target_file, self.DEFAULT_KEY, ["SEND_STRING(\"YOU PRESSED ANY KEY!\");"])
            for layerkey in sorted(scripts_dict.keys()):
                for scriptskey in sorted(scripts_dict[layerkey].keys()):
                    keycode = self.keycode(layerkey, scriptskey)
                    self.write_key_case(target_file, keycode, scripts_dict[layerkey][scriptskey].commands)
            target_file.write("\t}\n")
            target_file.write("\treturn true;\n")
            target_file.write("};\n")

    def write_key_case(self, target_file, key, commands):
        target_file.write("\t\tcase {}:\n".format(key))
        target_file.write("\t\t\tif (record->event.pressed) {\n")
        for command in commands:
            escaped_command = self.escape_quotes(str(command))
            target_file.write("\t\t\t\t{}\n".format(escaped_command))
        target_file.write("\t\t\t}\n")
        target_file.write("\t\t\tbreak;\n")

    def keycode(self , layerkey, scriptskey):
        return "_".join([layerkey, scriptskey])

    def escape_quotes(self, string):
        split = string.split('"')
        if len(split) > 3:
            return  "{}\"{}\"{}".format(split[0], "\\\"".join(split[1:-1]), split[-1])
        else:
            return string

if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser();
    argument_parser.add_argument("--scripts")
    argument_parser.add_argument("--target")
    args = argument_parser.parse_args()
    DuckyConvert(args.scripts, args.target).convert()
