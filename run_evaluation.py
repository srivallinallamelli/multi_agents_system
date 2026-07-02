from evaluation.dataset_generator import (
    generate_dataset
)

from evaluation.evaluator import (
    Evaluator
)


def main():

    print(
        "Generating evaluation dataset..."
    )

    generate_dataset(
        n=100
    )

    print(
        "Running evaluation..."
    )

    evaluator = Evaluator(
        "evaluation/dataset.csv"
    )

    evaluator.run()


if __name__ == "__main__":
    main()