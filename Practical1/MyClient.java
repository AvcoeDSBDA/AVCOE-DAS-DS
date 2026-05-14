public class MyClient {
 public static void main(String[] args) {
 try {
 MyInterface obj = (MyInterface)
java.rmi.Naming.lookup("//localhost/MyRemoteClass");
 System.out.println(obj.sayHello());
 } catch (Exception e) {
 e.printStackTrace();
 }
 }
} 
