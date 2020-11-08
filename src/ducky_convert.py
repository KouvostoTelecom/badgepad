import os
import sys
sys.path.append('/app/QuantumDuck/quantumduck')
import argparse
import quantum

class DuckyConvert:
    def __init__(self, scripts_dir):
        self.scripts_dir = scripts_dir

    def convert(self):
        converted = self.convert_scripts()
        keycode_enums = self.generate_enum_keycodes(converted)
        print(keycode_enums)

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
        # enum custom_keycodes {
        #                 NC
        #             };
        output = ["enum custom_keycodes {"]
        for layerkey in sorted(scripts_dict.keys()):
            for scriptskey in sorted(scripts_dict[layerkey].keys()):
                output.append("_".join([layerkey, scriptskey]))
        output.append("}")

        return output



if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser();
    argument_parser.add_argument("--scripts")
    args = argument_parser.parse_args()
    DuckyConvert(args.scripts).convert()
