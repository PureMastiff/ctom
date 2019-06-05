
#include <iostream>

using namespace std;


class Current18v
{
    public:
        virtual void useCurrent18v() = 0;
};


class Current220v
{
    public:
        virtual void useCurrent220v()
        {
            cout<<"我是220v 欢迎使用"<<endl;
        }
};


class Adapter: public Current18v
{
    public:
        Adapter(Current220v *current)
        {
            m_current = current;
        }
        virtual void useCurrent18v()
        {
            cout<<"适配器220v"<<endl;
            m_current->useCurrent220v();
        }
    private:
        Current220v *m_current;
};

int  main()
{
    Current220v *current220v = NULL;
    Adapter *adapter = NULL;

    current220v = new Current220v;
    adapter = new Adapter(current220v);
    adapter->useCurrent18v();

    delete current220v;
    delete adapter;
    cout<<"hello"<<endl;
    system("pause");
    return 0;
}
