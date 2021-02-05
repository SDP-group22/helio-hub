package com.helio.app.networking;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class HubClient {

    public HubClient(String baseAddress) {
        MotorService service = ServiceGenerator.createService(MotorService.class, baseAddress);
        Call<Motor> callAsync = service.getMotor(42);

        callAsync.enqueue(new Callback<Motor>() {
            @Override
            public void onResponse(Call<Motor> call, Response<Motor> response) {
                System.out.println(response);
                Motor motor = response.body();
            }

            @Override
            public void onFailure(Call<Motor> call, Throwable t) {
                System.out.println(t);
            }
        });
    }
}
