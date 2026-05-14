public class MyRemoteClass extends
java.rmi.server.UnicastRemoteObject implements MyInterface {
 public MyRemoteClass() throws java.rmi.RemoteException {
 super();
 }
 public String sayHello() throws java.rmi.RemoteException {
 return "Hello, world!";
 }
}
