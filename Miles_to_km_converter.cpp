#include <iostream>
#include <cmath>
using namespace std;
string elements[]={"to km","to miles"};
enum elements {km=1,miles=2};
void print_message()
{
    int x=1;
    cout<<"you want to convert \n";
    for (string element : elements)
    {
        cout<<x<<" "<<element<<"\n";
        x++;
    }
    cout<<endl;
}
int read_user_input()
{   
    int user_input;
    cin>>user_input;
    return user_input;
}
int is_input_valid()
{
    int user_input=read_user_input();
    if (user_input<1 || user_input>2)
    {
        return false;
    }
    else
    {
        return user_input;
    }
}
int get_user_input()
{
    int user_input;
    bool wrong_input=true;
    while (wrong_input)
    {
        user_input=is_input_valid();
        if (user_input==false)
        {
            cout<<"invalid_input"<<endl;
            wrong_input=true;
        }
        else
        {
            wrong_input=false;
        }
    }
    return user_input;
}
float get_first_element_value()
{
    float first_element;
    cout<<"enter the value of the first element"<<endl;
    cin>>first_element;
    return first_element;
}
float convert(float first_element,int user_choice)
{
    float result;
    if (user_choice==elements::km)
    {
        result=first_element*1.609344;
        return result;
    }
    if (user_choice==elements::miles)
    {
        result=first_element*0.6214;
        return result;
    }
}
int main()
{
    print_message();
    int user_choice=get_user_input();
    float first_element=get_first_element_value();
    float result=convert(first_element,user_choice);
    printf("result = %.*f\n",2,result);
    system("pause");
    return 0;
}