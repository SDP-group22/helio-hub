package com.helio.app;

import android.os.Bundle;
import android.os.Handler;
import android.view.MenuItem;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.navigation.NavController;
import androidx.navigation.Navigation;
import androidx.navigation.ui.AppBarConfiguration;
import androidx.navigation.ui.NavigationUI;

import com.google.android.material.bottomnavigation.BottomNavigationView;
import com.helio.app.model.Day;
import com.helio.app.model.Motor;
import com.helio.app.model.Schedule;
import com.helio.app.networking.HubClient;
import com.helio.app.networking.MoveMotorRequest;
import com.helio.app.networking.RegisterMotorRequest;
import com.helio.app.networking.RegisterScheduleRequest;
import com.helio.app.networking.RenameMotorRequest;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.atomic.AtomicInteger;

public class MainActivity extends AppCompatActivity {
    private Map<Integer, Motor> motors;
    private Map<Integer, Schedule> schedules;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Passing each menu ID as a set of Ids because each
        // menu should be considered as top level destinations.
        AppBarConfiguration appBarConfiguration = new AppBarConfiguration.Builder(
                R.id.navigation_control, R.id.navigation_blinds, R.id.navigation_hub)
                .build();
        NavController navController = Navigation.findNavController(this, R.id.nav_host_fragment);

        // This makes the bar at the top change when you use the navigation (changes the title text)
        NavigationUI.setupActionBarWithNavController(this, navController, appBarConfiguration);

        // This makes the fragment change when you press the navigation buttons
        BottomNavigationView navView = findViewById(R.id.nav_view);
        NavigationUI.setupWithNavController(navView, navController);

        fetchState();
    }

    @Override
    public boolean onOptionsItemSelected(@NonNull MenuItem item) {
        // Navigate backwards when pressing back button in top app bar
        if (item.getItemId() == android.R.id.home) {
            onBackPressed();
        }
        return super.onOptionsItemSelected(item);
    }

    private void fetchState() {
        motors = new HashMap<>();
        HubClient client = new HubClient("http://10.0.2.2:4310/");
        testMotor(client);
        testSchedule(client);
    }

    private void testMotor(HubClient client) {
        RegisterMotorRequest registerMotorRequest = new RegisterMotorRequest(
                "bedroom",
                "1.2.3.4",
                false,
                0, 0, 0, "style");
        // use Handler to force the actions to happen in order
        Handler handler = new Handler();
        handler.postDelayed(() -> client.addMotor(motors, registerMotorRequest), 0);

        // This is extremely bad
        AtomicInteger id = new AtomicInteger();

        handler.postDelayed(() -> id.set(new ArrayList<>(motors.keySet()).get(0)), 200);

        RenameMotorRequest renameMotorRequest = new RenameMotorRequest(id.get(), "kitchen");
        MoveMotorRequest moveMotorRequest = new MoveMotorRequest(id.get(), 25);
        handler.postDelayed(() -> client.activateMotor(motors, id.get()), 250);
        handler.postDelayed(() -> client.renameMotor(motors, renameMotorRequest), 500);
        handler.postDelayed(() -> client.getMotor(motors, id.get()), 750);
        handler.postDelayed(() -> client.moveMotor(motors, moveMotorRequest), 1000);
        handler.postDelayed(() -> client.startMotorCalibration(motors, id.get()), 1250);
        handler.postDelayed(() -> client.stopMotorCalibration(motors, id.get()), 1500);
        handler.postDelayed(() -> client.deactivateMotor(motors, id.get()), 1750);
        handler.postDelayed(() -> client.deleteMotor(motors, id.get()), 2000);
    }

    private void testSchedule(HubClient client) {
        schedules = new HashMap<>();
        List<Integer> motorIds = new ArrayList<>();
        motorIds.add(999);
        List<Day> days = new ArrayList<>();
        days.add(Day.MONDAY);
        RegisterScheduleRequest registerScheduleRequest = new RegisterScheduleRequest(
                "name",
                false,
                days,
                0, 0, motorIds, "16:20");

        // use Handler to force the actions to happen in order
        Handler handler = new Handler();
        handler.postDelayed(() -> client.addSchedule(schedules, registerScheduleRequest), 2250);

        // This is extremely bad
//        AtomicInteger id = new AtomicInteger();
//        handler.postDelayed(() -> id.set(new ArrayList<>(motors.keySet()).get(0)), 200);
//
//        RenameMotorRequest renameMotorRequest = new RenameMotorRequest(id.get(), "kitchen");
//        MoveMotorRequest moveMotorRequest = new MoveMotorRequest(id.get(), 25);
//        handler.postDelayed(() -> client.activateMotor(motors, id.get()), 250);
//        handler.postDelayed(() -> client.renameMotor(motors, renameMotorRequest), 500);
//        handler.postDelayed(() -> client.getMotor(motors, id.get()), 750);
//        handler.postDelayed(() -> client.moveMotor(motors, moveMotorRequest), 1000);
//        handler.postDelayed(() -> client.startMotorCalibration(motors, id.get()), 1250);
//        handler.postDelayed(() -> client.stopMotorCalibration(motors, id.get()), 1500);
//        handler.postDelayed(() -> client.deactivateMotor(motors, id.get()), 1750);
//        handler.postDelayed(() -> client.deleteMotor(motors, id.get()), 2000);
    }
}
