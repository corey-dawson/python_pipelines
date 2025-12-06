import argparse
from python_pipelines.transform import Pipeline, loader_map, exporter_map


def main(args: argparse.Namespace):
    
    # setup loader
    loader_cls = loader_map[args.loader]
    loader = loader_cls()
    
    # setup exporter
    exporter_cls = exporter_map[args.export]
    exporter = exporter_cls()
    
    # setup pipeline
    pipeline = Pipeline()
    
    # run pipeline
    pipeline.run(loader, exporter)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(
        description="Select a data loader and exporter for the pipeline."
    )
    parser.add_argument(
        '-l', 
        '--loader', 
        type=str,
        default='json',
        choices=loader_map.keys(),
        help=f"Specify the data loader to use: {', '.join(loader_map.keys())}"
    )
    parser.add_argument(
        '-e', 
        '--export', 
        type=str,
        default='skip',
        choices=exporter_map.keys(),
        help=f"Specify the exporter to use: {', '.join(exporter_map.keys())}"
    )
    parsed_args = parser.parse_args()
    main(parsed_args)