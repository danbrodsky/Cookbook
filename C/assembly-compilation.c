#include <stdio.h>

/* ------------------------------------------------------
 execute asm snippet
------------------------------------------------------ */
int asmSnippet() {
    int output, input;
    __asm__ volatile(" \
        pushf \n\
        pusha \n\
        popf  \n\
        popa  \n\
        mov input, %%eax \n\
        mov %%eax, output \n\
        "
        : "=g"(output) 
        : "g"(input)
        : "%eax"
        );
    return 0;
}

/* ------------------------------------------------------
 convert asm to shared library
------------------------------------------------------ */
// > nasm -f elf32 <asm-file> -o module.o
#include <stdio.h>
extern int function(int arg);


int main(void) {

	printf("%x\n", function(0));

	return 0;
}
// > gcc runAsm.c module.o -o runAsm -m32


/* ------------------------------------------------------
 convert and run asm as shellcode
------------------------------------------------------ */

// > convert assembly to shellcode @ defuser.ca

char shellcode[] = "<target-shellcode>";

void main2(int argc, char **argv) {
    int (*fp) (int);
    fp = (void *)shellcode;
    printf("%x\n", fp(0));
}

// > gcc runShellcode.c -o runShellcode -fno-stack-protector -z execstack -no-pie -m32
