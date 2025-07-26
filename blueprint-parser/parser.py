import yaml
import sys

def load_blueprint(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def generate_pipeline(blueprint):
    language = blueprint['language']
    stages = blueprint.get('stages', [])

    output = []

    # Add language base setup
    with open(f'templates/{language}.yml', 'r') as f:
        output.append(f.read())

    # Add each stage
    for stage in stages:
        with open(f'templates/shared/{stage}.yml', 'r') as f:
            output.append(f.read())

    return '\n'.join(output)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python parser.py <blueprint-file>")
        sys.exit(1)

    blueprint_file = sys.argv[1]
    blueprint = load_blueprint(blueprint_file)
    pipeline_yaml = generate_pipeline(blueprint)

    with open('generated-pipeline.yml', 'w') as f:
        f.write(pipeline_yaml)

    print("✅ Pipeline generated: generated-pipeline.yml")

