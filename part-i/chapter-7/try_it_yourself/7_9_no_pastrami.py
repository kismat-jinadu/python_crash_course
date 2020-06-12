sandwich_orders=['pastrami','chicken','beef','pastrami','egg','pastrami','tuna']

print("The deli has run out of pastrami")

finished_sandwiches= []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:    
    sandwiches = sandwich_orders.pop()

    print(f"I made your {sandwiches.title()} sandwich")
    finished_sandwiches.append(sandwiches)

print("\nCompleted order:")
for finished_sandwich in finished_sandwiches: 
    print(f"\n{finished_sandwich.title()} sandwich")