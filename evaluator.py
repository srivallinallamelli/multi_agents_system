import json
import pandas as pd

from tqdm import tqdm

from graph.evaluation_workflow import build_evaluation_graph

class Evaluator:

    def __init__(self, dataset_path):

        self.dataset = pd.read_csv(
            dataset_path
        )

        self.workflow = build_evaluation_graph()

    def normalize(self, value):

        try:

            if isinstance(value, str):

                value = eval(value)

            if isinstance(value, list):

                value = sorted(
                    value,
                    key=lambda x: str(x)
                )

            return json.dumps(
                value,
                sort_keys=True
            )

        except Exception:

            return str(value)

    def run(self):

        scores = []

        for _, row in tqdm(
            self.dataset.iterrows(),
            total=len(self.dataset)
        ):

            state = {
                "query": row["query"]
            }

            result = self.workflow.invoke(
                state
            )

            actual_output = self.normalize(
                result.get(
                    "output",
                    []
                )
            )

            expected_output = self.normalize(
                row["expected_output"]
            )

            score = (
                1
                if actual_output ==
                expected_output
                else 0
            )

            scores.append(score)

        accuracy = (
            sum(scores)
            / len(scores)
        )

        print("\n====================")
        print(" EVALUATION REPORT ")
        print("====================")

        print(
            f"Total Queries : {len(scores)}"
        )

        print(
            f"Correct : {sum(scores)}"
        )

        print(
            f"Incorrect : "
            f"{len(scores)-sum(scores)}"
        )

        print(
            f"Accuracy : "
            f"{accuracy:.2%}"
        )

        if accuracy >= 0.80:

            print(
                "STATUS : PASSED"
            )

        else:

            print(
                "STATUS : FAILED"
            )

        return accuracy