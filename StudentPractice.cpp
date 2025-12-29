#include <iostream>
#include <sstream>

using namespace std;

class Student{

    private:
        int m_age;
        string m_first_name;
        string m_last_name;
        int m_standard;

    
    public:
        void set_age(int age){
            m_age = age;
        }

        int get_age(){
            return m_age;
        }

        void set_last_name(string last_name){
            m_last_name = last_name;
        }

        string get_last_name(){
            return m_last_name;
        }

        void set_first_name(string first_name){
            m_first_name = first_name;
        }

        string get_first_name(){
            return m_first_name;
        }

        void set_standard(int standard){
            m_standard = standard;
        }

        int get_standard(){
            return m_standard;
        }

        string to_string(){
            stringstream ss;
            ss << m_age << "," << m_first_name << ","<< m_last_name << ","<< m_standard;

            string result = ss.str();
            return result;
        }
};



int main(){

    int age,standard;
    string first_name,last_name;

    cin >> age >> first_name >> last_name >> standard;

    Student st;
    st.set_age(age);
    st.set_standard(standard);
    st.set_first_name(first_name);
    st.set_last_name(last_name);
    
    cout << st.get_age() << "\n";
    cout << st.get_last_name() << ", " << st.get_first_name() << "\n";
    cout << st.get_standard() << "\n";
    cout << "\n";
    cout << st.to_string();

    return 0;
}


