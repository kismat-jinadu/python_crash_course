sandwich_orders=['chicken','beef','egg','tuna']

finished_sandwiches= []

while sandwich_orders:
    sandwiches = sandwich_orders.pop()

    print(f"I made your {sandwiches.title()} sandwich")
    finished_sandwiches.append(sandwiches)

print("\nCompleted order:")
for finished_sandwich in finished_sandwiches: 
    print(f"\n{finished_sandwich.title()} sandwich")