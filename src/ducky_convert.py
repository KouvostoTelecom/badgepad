import os
import sys
sys.path.append('/app/QuantumDuck/quantumduck')
import argparse
import quantum

class DuckyConvert:
    DEFAULT_KEY = "ANY_KEY"

    def __init__(self, scripts_dir):
        self.scripts_dir = scripts_dir

    def convert(self):
        converted = self.convert_scripts()
        keycode_enums = self.generate_enum_keycodes(converted)
        print(keycode_enums)
        keymap = self.generate_keymap(converted)
        print(keymap)

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

    def generate_enum_keycodes(self, scripts_dict):
        output = ["enum custom_keycodes {"]
        output.append(self.DEFAULT_KEY)
        for layerkey in sorted(scripts_dict.keys()):
            for scriptskey in sorted(scripts_dict[layerkey].keys()):
                output.append(self.keycode(layerkey, scriptskey))
        output.append("}")

        return output

    def generate_keymap(self, scripts_dict):
        output = ["const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {"]
        for layer_index, layerkey in enumerate(sorted(scripts_dict.keys())):
            keys = sorted(scripts_dict[layerkey].keys())[:8]
            num_of_scripts  = len(keys)

            # for script_index, scriptskey in enumerate(sorted(scripts_dict[layerkey].keys())):
                       # jkk[1] = LAYOUT(
                  # ),
            output.append("[{}]  = LAYOUT(".format(layer_index))
            output.append("""
                         {},             {},
                   {},       {}, {},       {},
                         {},             {}
                          """.format(
                              self.keycode(layerkey, keys[0]) if 0 < num_of_scripts else self.DEFAULT_KEY,
                              self.keycode(layerkey, keys[1]) if 1 < num_of_scripts else self.DEFAULT_KEY,
                              self.keycode(layerkey, keys[2]) if 2 < num_of_scripts else self.DEFAULT_KEY,
                              self.keycode(layerkey, keys[3]) if 3 < num_of_scripts else self.DEFAULT_KEY,
                              self.keycode(layerkey, keys[4]) if 4 < num_of_scripts else self.DEFAULT_KEY,
                              self.keycode(layerkey, keys[5]) if 5 < num_of_scripts else self.DEFAULT_KEY,
                              self.keycode(layerkey, keys[6]) if 6 < num_of_scripts else self.DEFAULT_KEY,
                              self.keycode(layerkey, keys[7]) if 7 < num_of_scripts else self.DEFAULT_KEY
                          ))
            output.append("),")
        output.append("}")

        return output

    def keycode(self , layerkey, scriptskey):
        return "_".join([layerkey, scriptskey])






if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser();
    argument_parser.add_argument("--scripts")
    args = argument_parser.parse_args()
    DuckyConvert(args.scripts).convert()
