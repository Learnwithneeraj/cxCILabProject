import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;
import org.apache.jasper.runtime.*;
import org.owasp.esapi.ESAPI;
import cnt.Security.*;

public class BookDetail_jsp extends HttpJspBase {

  public static String loadDriver () {
		// flow example
		
		String a = request.getParameter("age"); // input
		int b = (Int)a * 2;
		out.println(a); // potential XSS
		out.println(b); // printing a number
	}
	
	private static void printSanitizedName (String str) {

		String sanitizedUserData = Security.validName(str);
		out.println (sanitizedUserData);
	}

	public static void loadData () {

		String userData = request.getParameter("Data"); 
		out.println (userData);

		printSanitizedName(userData);
	}

}
