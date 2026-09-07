def find_common_intelligence(registry):
    knowledge_sets = [
            agent_data["Knowledge"] for agent_data in registry.values()
        ]
    return set.intersection(*knowledge_sets)

def relocate_agent(registry, log, agent_id, new_location):
    try:
        print("Attempting direct mutation of Agent_Alpha’s Location tuple...")
        registry[agent_id]["Location"][0] = new_location[0]
    except TypeError as t:
        print(t)
        print("Tuples are immutable; reassigninga new tuple instead.")
        registry[agent_id]["Location"] = new_location
        log.setdefault(agent_id, []).append(new_location)
        print(log)
        
    

agent_registry = {
    "Agent_Alpha": {
        "Location": (10, 20),
        "Knowledge": {
            "grid map",
            "comm protocol",
            "telemetry sync"
        }
    },

    "Agent_Beta": {
        "Location": (15, 5),
        "Knowledge": {
            "grid map",
            "comm protocol",
            "power grid"
        }
    },

    "Agent_Gamma": {
        "Location": (0, 0),
        "Knowledge": {
            "grid map",
            "comm protocol",
            "power grid",
            "telemetry sync"
        }
    }
}

print("--- Common Intelligence Across All Agents ---")
print(find_common_intelligence(agent_registry))

print("\n\n--- Relocating Agent_Alpha ---")
log={}
relocate_agent(agent_registry, log, "Agent_Alpha", (12,22))
relocate_agent(agent_registry, log, "Agent_Alpha", (22,35))

summary_report= {
    agent_id : len(data["Knowledge"])
    for agent_id, data in agent_registry.items()
    }

print("--Summary Report ( Dictionary Comprehension )--")
print(summary_report)

