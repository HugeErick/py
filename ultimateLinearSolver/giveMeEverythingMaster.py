from giveMeEverything import solveMultipleSystems
from equations import systems, systems1, rep

def main():
    with open("eqLog.md", "w") as file:
        file.write("# Erick Gonzalez Parada | Partial Exam II | 178145\n")
        file.write("## Solving the Matrix Systems\n\n")
        
        solveMultipleSystems(rep, file)

if __name__ == "__main__":
    main()

