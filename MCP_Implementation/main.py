from mcp.server.fastmcp import FastMCP
from typing import List, Dict
import logging

reciepes: Dict[str, List[str]] = {
    "Pasta": ["Boil water", "Add pasta", "Cook for 10 minutes", "Drain water", "Add sauce"],
    "Salad": ["Chop vegetables", "Add dressing", "Toss salad"],
    "Sandwich": ["Take two slices of bread", "Add fillings", "Close sandwich"],
    "Soup": ["Boil water", "Add ingredients", "Cook for 20 minutes", "Serve hot"],
    "Pizza": ["Prepare dough", "Add toppings", "Bake in oven for 15 minutes", "Serve hot"],
    "Burger": ["Prepare patty", "Grill patty", "Assemble burger with bun and toppings", "Serve hot"],
    "Tacos": ["Prepare tortillas", "Add fillings", "Fold tortillas", "Serve hot"],
    "Curry": ["Prepare ingredients", "Cook spices", "Add ingredients", "Simmer for 30 minutes", "Serve hot"],
    "Stir Fry": ["Chop vegetables", "Heat oil in pan", "Add vegetables", "Stir fry for 5 minutes", "Serve hot"],
    "Pancakes": ["Mix ingredients", "Heat pan", "Pour batter", "Cook for 2 minutes on each side", "Serve hot with syrup"]
}

# Create MCP server
mcp = FastMCP("Reciepes", "A simple reciepe management system")

# Tool to get reciepe steps
@mcp.tool(
    name="get_reciepe_steps", description="Get the steps for a given reciepe")
def get_reciepe_steps(reciepe_name: str) -> List[str]:
    if reciepe_name in reciepes:
        return reciepes[reciepe_name]
    else:
        return ["Reciepe not found"]

# Tool to add a new reciepe
@mcp.tool(
    name="add_reciepe", description="Add a new reciepe with steps")
def add_reciepe(reciepe_name: str, steps: List[str]) -> str:
    if reciepe_name in reciepes:
        return "Reciepe already exists"
    else:
        reciepes[reciepe_name] = steps
        return "Reciepe added successfully"

# Tool to delete a reciepe
@mcp.tool(
    name="delete_reciepe", description="Delete a reciepe")
def delete_reciepe(reciepe_name: str) -> str:
    if reciepe_name in reciepes:
        del reciepes[reciepe_name]
        return "Reciepe deleted successfully"
    else:
        return "Reciepe not found"

# Tool to list all reciepes
@mcp.tool(
    name="list_reciepes", description="List all available reciepes")
def list_reciepes() -> List[str]:
    return list(reciepes.keys())

# Resource to expose all recipes as readable data
@mcp.resource(
    uri="recipe://recipes",
    name="recipes",
    description="View all available recipes"
)
def recipes_resource() -> Dict[str, List[str]]:
    return reciepes

if __name__ == "__main__":
    logging.info("Starting Reciepe Management MCP Server...")
    logging.info("Registered tools: get_reciepe_steps, add_reciepe, delete_reciepe, list_reciepes")
    logging.info("Transport: stdio")
    logging.info("Waiting for an MCP client to connect...")

    mcp.run()
