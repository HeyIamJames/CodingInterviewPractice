using std::cout;
using std::endl;

void Question1_2::reverse(char* str) 
{
    char *ptrEnd = str;
    char temp;

    if (str) 
    {
        while (*ptrEnd) 
        {
            ptrEnd++;
        }
        ptrEnd--;

        while (str < ptrEnd) 
        {
            temp = *str;
            *str++ = *ptrEnd;
            *ptrEnd-- = temp;
        }
    }
}
