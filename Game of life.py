# Import appropriate librarie
import copy

# LIVE and DEAD, two global constants to make it easy to change for testing (in case the values used are not the same as mine)
LIVE = "l"
DEAD = "d"
nextState = []

def main():
    # Best to request user input instead of hard copying an initialState
    # And then make sure the user respects the required criteria: 2D list with only "l" or "d" values (unless change the global constants)
    # To make it easier to check the code directly, I have included an initial state in the code 
    # This organism dies in 4 steps
    initialState = [
        [LIVE, DEAD, DEAD, DEAD, LIVE],
        [LIVE, LIVE, LIVE, LIVE, LIVE],
        [LIVE, DEAD, DEAD, DEAD, LIVE], 
        [LIVE, LIVE, LIVE, LIVE, LIVE], 
        [LIVE, DEAD, DEAD, LIVE, LIVE]
    ]

    # Print the initial state
    print("Initial state: ")
    for i in range(len(initialState)):
        print(initialState[i])
    print("\nNext stage: ")

    # Get the next stage
    nextStateCreator(initialState)
    
    while True: 
        # Check that the organism is not dead
        organismIsDead = True

        for i in range(len(nextState)):
            if nextState[i].count(LIVE) != 0:
                organismIsDead = False

        # If the organism is still alive, ask if the next stage is required
        if organismIsDead == False:
            response = input("Would you like to see the next state for this life form (y/n): ")
            if response.lower().count("n") == 0:
                newState = copy.deepcopy(nextState)
                nextState.clear()
                # Get the next stage
                nextStateCreator(newState)
            else:
                break
        # If the organism is dead
        else:
            print("This organim is dead.\n")
            break 

# Figure out the next stage and print it in the terminal
def nextStateCreator(initialState):
    for i in range(len(initialState)):
        newRow = []

        for j in range(len(initialState[i])):
            # Set a list of all the cells surrounding the current cell
            snapshot =[]
            rows = [i-1, i, i+1]
            columns = [j-1, j, j+1]

            # Making sure the rows and columns are not out of index range
            for row in rows:
                # Skip if the row is out of index range
                if row < 0 or row >= len(initialState):
                    pass
                else:
                    for column in columns:
                        # Skip if the column is out of index range
                        if column < 0 or column >= len(initialState[i]):
                            pass
                        # Skip the current cell
                        elif row == i and column == j:
                            pass
                        else:
                            snapshot.append(initialState[row][column])

            # Count the number of live cells
            x = snapshot.count(LIVE)

            # Enter the current cell into the new state row based on the evolution rules
            if (initialState[i][j] == DEAD and x == 3) or (initialState[i][j] == LIVE and (x == 2 or x == 3)):
                newRow.append(LIVE)
            else:
                newRow.append(DEAD)
        
        # Add the row to the new state grid
        nextState.append(newRow)

    # Print the new state
    for i in range(len(nextState)):
        print(nextState[i])


if __name__ == "__main__":
    main()