#include <stdio.h>
#include <inttypes.h>
#include <string.h>

/*

USE ARRAYS FOR NUMERATOR AND DENOMINAROR TO KEEP TRAKC OF FRACTIONS




*/
struct _Node {
	char* key;                  // ptr to proper C-string
	uint32_t* locations;        // ptr to dynamic array of string locations
								// -> all locations which match a given key 
	uint32_t numLocations;      // number of elements currently in locations array
	uint32_t maxLocations;      // dimension of locations array
	struct _Node* next;   // ptr to next node object in table slot
};
typedef struct _Node Node;


struct _HashTable {
	Node** table;       // physical array for table
	uint32_t tableSz;         // number of slots in the table
	uint32_t numEntries;      // number of entries in the table (not
	                          //   necessarily the number of nonempty slots)
	uint32_t (*hash)(const char* str);   // pointer to the hash function
};
typedef struct _HashTable HashTable;

int gcd(int a, int b) {
    int t = b;
    while (b != 0) { 
        t = b;
        b = a % b;
        a = t;
    }
    return a;
}

/** Hashes a C-string to an unsigned integer.
 *  Pre:
 *       str points to a zero-terminated char array
 */
uint32_t elfhash(const char* str) {
    // self-destuct if called with NULL
    assert(str != NULL);     

    // value to be returned and high nybble of current hashvalue
    uint32_t hashvalue = 0, high;             
            
    // continue until *str is '\0'hashvalue = (hashvalue << 4) + *str++; 
    // shift high nybble out,   
    // and add in next char 
    // if high nybble != 0000 -> fold it back in
    // zero high nybble
    while (*str) {                                
        if ( (high = (hashvalue & 0xF0000000)) ) {  
            hashvalue = hashvalue ^ (high >> 24);  
        }
        hashvalue = hashvalue & 0x7FFFFFFF;         
    }
    return hashvalue;
}

int main() {
    int T = 12000;
    int S = 0;

}