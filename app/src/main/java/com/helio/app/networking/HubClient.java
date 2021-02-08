package com.helio.app.networking;

import java.io.IOException;
import java.util.Map;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class HubClient {
    private final HubService service;

    public HubClient(String baseAddress) {
        service = ServiceGenerator.createService(HubService.class, baseAddress);
    }

    public void getMotor(int motorId, Map<Integer, Motor> motors) {
        Call<Motor> call = service.getMotor(motorId);

        call.enqueue(new Callback<Motor>() {
            @Override
            public void onResponse(Call<Motor> call, Response<Motor> response) {
                Motor m = response.body();
                if(m != null) {
                    System.out.println(call + " succeeded: " + m);
                    motors.put(motorId, m);
                }
            }

            @Override
            public void onFailure(Call<Motor> call, Throwable t) {
                System.out.println(call + " failed: " + t);
            }
        });
    }
}
