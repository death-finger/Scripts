#include "number.h"
#include "stdio.h"

Number::Number(int start) {
    data = start;
    printf("Number: %d\n", data);
}

Number::~Number() {
    printf('~Number: %d\n', data);
}

void Number::add(int value) {
    data += value;
    printf("add %d\n", value);
}

