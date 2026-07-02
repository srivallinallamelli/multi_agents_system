from graph.workflow import build_graph

workflow = build_graph()


def main():

    print("\n===================================")
    print(" EMPLOYEE ANALYTICS MULTI AGENT ")
    print("===================================\n")

    print("Type 'exit' to quit.\n")

    while True:

        query = input("Ask Question: ")

        if query.lower() == "exit":
            print("\nGoodbye!")
            break

        state = {
            "query": query
        }

        result = workflow.invoke(state)

        print("\n-----------------------------")

        print("Intent:")
        print(result.get("intent"))

        print("\nGenerated SQL:")
        print(result.get("sql"))

        print("\nAnswer:")
        print(result.get("final_answer"))

        print("\n-----------------------------\n")


if __name__ == "__main__":
    main()