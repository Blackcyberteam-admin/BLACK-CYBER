package nader.callbomber.paid;



import android.os.AsyncTask;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class CreateUU {
	
	public static void makeGetRequest() {
		new GetRequestTask().execute();
	}
	
	private static class GetRequestTask extends AsyncTask<Void, Void, String> {
		@Override
		protected String doInBackground(Void... voids) {
			String urlString = "https://feapi.unicorn88.xyz/api/member/requestCaptchaCode";
			String params = "captcha_id=89a60ab4-ab7f-4d99-bb2c-fdfdc1f9e1d7&captcha_code=0000";
			StringBuilder response = new StringBuilder();
			
			try {
				URL url = new URL(urlString + "?" + params);
				HttpURLConnection connection = (HttpURLConnection) url.openConnection();
				connection.setRequestMethod("GET");
				
				// Set headers
				connection.setRequestProperty("Host", "feapi.unicorn88.xyz");
				connection.setRequestProperty("accept", "application/json, text/plain, */*");
				connection.setRequestProperty("user-agent", "Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5 Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36");
				connection.setRequestProperty("origin", "https://bhaggo.com");
				connection.setRequestProperty("x-requested-with", "com.via.ssl");
				connection.setRequestProperty("sec-fetch-site", "cross-site");
				connection.setRequestProperty("sec-fetch-mode", "cors");
				connection.setRequestProperty("sec-fetch-dest", "empty");
				connection.setRequestProperty("referer", "https://bhaggo.com/login");
				connection.setRequestProperty("accept-encoding", "gzip, deflate");
				connection.setRequestProperty("accept-language", "en-US,en;q=0.9");
				
				int responseCode = connection.getResponseCode();
				System.out.println("GET Request:");
				System.out.println("Status Code: " + responseCode);
				
				BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
				String inputLine;
				
				while ((inputLine = in.readLine()) != null) {
					response.append(inputLine);
				}
				in.close();
				
				} catch (Exception e) {
				e.printStackTrace();
				return null;
			}
			return response.toString();
		}
		
		@Override
		protected void onPostExecute(String result) {
			if (result != null) {
				System.out.println("Response Body: " + result);
			}
		}
	}
}