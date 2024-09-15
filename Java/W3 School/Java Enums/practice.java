class MultiThreadingDemo implements Runnable {
	@Override
	public void run() {
		try{
			System.out.println("The Current Thread is: " + Thread.currentThread().getId());
		} catch(Exception e){
			System.out.println("Exception was caught and exception is: " + e);
		}
	}
}

public class practice {
	public static void main(String[] args) {
		int n = 8;
		for (int i = 0; i < n; i++) {
			Thread obj = new Thread(new MultiThreadingDemo());
			obj.start();
		}
	}
}
