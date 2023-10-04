#include <iostream>
#include <stdio.h>
#include <windows.h>
#include <time.h>
#include <cmath>
#include <chrono>

using namespace std;

char* createString(int size) {
    int N = size;
    char str[]{ "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" };
    int strN = 62;
    srand(time(NULL));
    char* pass = new char[N + 1];
    for (int i = 0; i < N; i++)
    {
        pass[i] = str[rand() % strN];
    }
    pass[N] = 0;
    return pass;
}

void selectionString(int passwordLenght, string password) {
    std::string str_password = password;

    std::string str_chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789";

    bool cycle = true;
    bool founded = false;
    int size_password = passwordLenght;
    int size_chars = str_chars.size();
    int *indexer = new int[size_password];
    std::string str_bruteforce;
    str_bruteforce.resize(size_password);
    for (int i = 0; i < size_password; ++i) indexer[i] = 0;

    std::cout << "Alphabet: " << str_chars << std::endl;
    std::cout << "Lenght of password: " << size_password << std::endl;
    std::cout << "Length of alpabet: " << size_chars << std::endl;
    std::cout << "Number of variants password: " << std::pow(size_chars, size_password) << std::endl; // variants = library ^ password
    std::cout << "Please wait..." << std::endl;

    while (true) {
        for (int i = size_password - 1; i >= 0; --i) {
            if (i != 0) {
                if (indexer[i] == size_chars) {
                    indexer[i] = 0;
                    indexer[i - 1]++;
                }
            }
        }

        for (int i = 0; i < size_password; ++i) str_bruteforce[i] = str_chars[indexer[i]];

        cycle = true;
        if (str_bruteforce == str_password) {
            std::cout << "You password: " << str_bruteforce << std::endl;
            cycle = false;
            founded = true;
        } if (!cycle) break;

        cycle = false;
        for (int i = 0; i < size_password; ++i) {
            if (indexer[i] != size_chars - 1) {
                cycle = true;
                break;
            }
        } if (!cycle) break;

        indexer[size_password - 1]++;
    }
    if (!founded) std::cout << "Error selected characters" << std::endl;
}

int main()
{
    int passLenght;
    cout << "Enter pass lenght: ";
    cin >> passLenght;

    auto start_time = std::chrono::high_resolution_clock::now();    

    char* pass = createString(passLenght);
    cout << pass << endl;
    selectionString(passLenght, pass);

    auto end_time = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time);
    std::cout << "Time: " << duration.count() << " microseconds" << std::endl;

    return 0;
}