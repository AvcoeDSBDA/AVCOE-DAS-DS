public class MyServer {
 public static void main(String[] args) {
 try {
 MyInterface obj = new MyRemoteClass();
 java.rmi.registry.LocateRegistry.createRegistry(1099);
 java.rmi.Naming.rebind("//localhost/MyRemoteClass", obj);
 System.out.println("MyRemoteClass bound in registry");
 } catch (Exception e) {
 System.err.println("MyRemoteClass exception:");
 e.printStackTrace();
 }
 } 
}