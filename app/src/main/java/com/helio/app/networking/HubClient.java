package com.helio.app.networking;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class HubClient {

    public HubClient(String baseAddress) {
        MotorService service = ServiceGenerator.createService(MotorService.class, "");
        Call<Motor> callAsync = service.getMotor(42);

        callAsync.enqueue(new Callback<Motor>() {
            @Override
            public void onResponse(Call<Motor> call, Response<Motor> response) {
                Motor motor = response.body();
                System.out.println(response.body());
            }

            @Override
            public void onFailure(Call<Motor> call, Throwable t) {
                System.out.println(t);
            }
        });
    }
}
