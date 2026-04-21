import json
from collections import defaultdict

# Load JSON Tree File
with open("reflection-tree.json", "r", encoding="utf-8") as file:
    data = json.load(file)

nodes = {node["id"]: node for node in data["nodes"]}

# State Tracking
state = {
    "answers": {},
    "signals": defaultdict(int)
}

# Helper Functions
def apply_signals(signal_list):
    """Add signal counts to state"""
    for signal in signal_list:
        state["signals"][signal] += 1


def dominant(axis_name):
    """Find dominant signal in an axis"""
    options = {
        key.split(":")[1]: value
        for key, value in state["signals"].items()
        if key.startswith(axis_name + ":")
    }

    if not options:
        return "balanced"

    return max(options, key=options.get)


def show_summary(text):
    """Replace placeholders in summary"""
    text = text.replace("{axis1}", dominant("axis1"))
    text = text.replace("{axis2}", dominant("axis2"))
    text = text.replace("{axis3}", dominant("axis3"))
    return text



# Main Engine
current = "START"

while True:
    node = nodes[current]
    node_type = node["type"]

    print("\n" + "-" * 60)
    print(node["text"])

    
    # START / BRIDGE / REFLECTION
    if node_type in ["start", "bridge", "reflection"]:
        input("\nPress Enter to continue...")
        current = node["next"]


    # QUESTION
    elif node_type == "question":
        options = node["options"]

        for i, option in enumerate(options, start=1):
            print(f"{i}. {option['text']}")

        while True:
            try:
                choice = int(input("\nChoose option number: "))
                if 1 <= choice <= len(options):
                    break
                else:
                    print("Invalid choice.")
            except:
                print("Enter a valid number.")

        selected = options[choice - 1]

        # Save answer
        state["answers"][current] = selected["text"]

        # Apply signals if present
        if "signal" in selected:
            apply_signals(selected["signal"])

        # Go next
        if "next" in selected:
            current = selected["next"]
        else:
            current = node["next"]

    
    # SUMMARY
    elif node_type == "summary":
        print("\n" + show_summary(node["text"]))
        input("\nPress Enter to continue...")
        current = node["next"]


    # END
    elif node_type == "end":
        print("\nSession complete.")
        break