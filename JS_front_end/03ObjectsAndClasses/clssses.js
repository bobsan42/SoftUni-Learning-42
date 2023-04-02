
// CLASSES
class Student {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    sayHello() {
        console.log(`Hello, my name is ${this.name}. I am ${this.age} years old.`)
    }
};

const stu = new Student('Kiro', 42);
console.log(stu.name, stu.age);
stu.sayHello();

console.log(typeof Student);
console.log(typeof stu);

class Dog {
    constructor(name) {
        this.name = name;
    }
    speak() {
        console.log(`${this.name} says Woof!`);
    }
}
let dog = new Dog('Sparky');
dog.speak(); // Sparky says Woof!
