#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

// Part 1

// Return type must be declared before the function
// * indicate that the variable is a pointer
int get_num(const char *line) {

    char first = 0, last = 0;

    // Loop through chars in string until end ('\0')
    for (int i = 0; line[i] != '\0'; i++) // i++ keeps track of loop iterations

        // Similar to Python, shocking
        if (isdigit(line[i])) {
            first = line[i];
            break;
        }

    for (int i = strlen(line) - 1; i >= 0; i--) // Going backwards (finding last digit)
        if (isdigit(line[i])) {
            last = line[i];
            break; 
        }
        
    // Use '?' as ternary operator (if, else) and atoi (=int() (Python))
    return (first != 0 && last != 0) ? atoi((char[]){first, last, '\0'}) : 0;
    // atoi = int()
}

int main() {
    int ans = 0;
    FILE *file = fopen("data/puzzle_1.txt", "r");

    // Arrays require a pre-allocated size whichmust be known at compile time
    char line[256]; // Declare an array to store each line in the file (buffer size: 256)
    while (fgets(line, sizeof(line), file) != NULL)
        ans += get_num(line);

    fclose(file); // C convention, else cause leakage (?)

    // %f\n simply to print value of n
    printf("Total: %d\n", ans);

    return 0;
}