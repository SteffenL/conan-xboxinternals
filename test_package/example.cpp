#include <Cryptography/XeCrypt.h>

#include <iostream>

int main() {
    unsigned char data[8];
    XeCrypt::BnQw_SwapDwQwLeBe(data, sizeof(data));
    std::cout << "Xbox Internals library works!" << std::endl;
    return 0;
}
