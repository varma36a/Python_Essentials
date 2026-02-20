

class Person {

    String name;
    int age;

    // Constructor
    Person(String n, int a) {
        name = n;
        age = a;
    }
   
    void display() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }

    public static void main(String[] args) {
        Person p1 = new Person("Rohith", 26);
        p1.display();
    }
}