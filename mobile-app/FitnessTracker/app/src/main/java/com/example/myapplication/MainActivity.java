package com.example.myapplication;

// Import the required libraries
import androidx.appcompat.app.AppCompatActivity;
import android.graphics.Color;
import android.os.Bundle;
import android.os.Handler;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import org.eazegraph.lib.charts.BarChart;
import org.eazegraph.lib.models.BarModel;

import java.io.IOException;


import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.OkHttpClient;
import okhttp3.Request;

import okhttp3.Response;

public class MainActivity
        extends AppCompatActivity {

    int flag=0;
    public String baseURL ="http://34.122.209.252/";
    public String yestWalkURL= baseURL+"yesterdays_walk_count";
    public String yestRunURL= baseURL+"yesterdays_run_count";
    public String todayWalkURL= baseURL+"todays_walk_count";
    public String todayRunURL= baseURL+"todays_run_count";
    public String currentActivityURL= baseURL+"current_activity";

    // Create the object of TextView
    // and PieChart class
    TextView tvWalk, tvRun,currentActivity;
    BarChart barchart;

    Button todaysData, yesterdaysData;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Link those objects with their
        // respective id's that
        // we have given in .XML file
        tvWalk = (TextView) findViewById(R.id.tvWalk);
        tvRun = findViewById(R.id.tvRun);
        currentActivity =findViewById(R.id.currentActivity);
        barchart = findViewById(R.id.barchart);

        // Creating a method setData()
        // to set the text in text view and pie chart
        try {
            setData(tvWalk,yestWalkURL,0);
            setData(tvRun,yestRunURL,0);

        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    public void setData(TextView view, String URL, int flag) throws IOException {
        OkHttpClient client = new OkHttpClient();
        client = new OkHttpClient();
        Request request = new Request.Builder().url(URL).build();

        client.newCall(request).enqueue(new Callback() {
            @Override
            public void onFailure(Call call, IOException e) {
                call.cancel();
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                String myResponse = response.body().string().trim();
                MainActivity.this.runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        if(flag== 1) {
                            String prediction= myResponse.substring( 1, myResponse.length() - 1 );
                            if (prediction.equals("1")){ view.setText("Running"); }
                            if (prediction.equals("0")){ view.setText("Walking"); }
                        }else if(flag==0){
                            view.setText(myResponse);
                        }
                    }
                });
            }
        });
    }

    Handler handler = new Handler();
    Runnable runnable;
    int delay = 15*1000; //Delay for 15 seconds.  One second = 1000 milliseconds.


    @Override
    protected void onResume() {
        //start handler as activity become visible
        //Refresh current activity data every 15 secs
        handler.postDelayed( runnable = new Runnable() {
            public void run() {
                try {
                    setData(currentActivity,currentActivityURL,1);
                } catch (IOException e) {
                    e.printStackTrace();
                }
                handler.postDelayed(runnable, delay);
            }
        }, delay);

        super.onResume();
    }

// If onPause() is not included the threads will double up when you
// reload the activity

    @Override
    protected void onPause() {
        handler.removeCallbacks(runnable); //stop handler when activity not visible
        super.onPause();
    }


    private void setBarChartData(int walk,int run) {
        barchart.clearChart();

        barchart.addBar(
                new BarModel(
                        "Walk",
                        walk,
                        Color.parseColor("#fb7268")));
        barchart.addBar(
                new BarModel(
                        "Run",
                        run,
                        Color.parseColor("#05af9b")));

        // To animate the bar chart
        barchart.startAnimation();
    }

    public void getYesterday(View view) {

        try {
            setData(tvWalk,yestWalkURL,0);
            setData(tvRun,yestRunURL,0);
            int walk = Integer.parseInt(tvWalk.getText().toString());
            int run  = Integer.parseInt(tvRun.getText().toString());
            setBarChartData(walk,run);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }


    public void getToday(View view) {
        try {
            setData(tvWalk,todayWalkURL,0);
            setData(tvRun,todayRunURL,0);
            int walk = Integer.parseInt(tvWalk.getText().toString());
            int run  = Integer.parseInt(tvRun.getText().toString());
            setBarChartData(walk,run);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
