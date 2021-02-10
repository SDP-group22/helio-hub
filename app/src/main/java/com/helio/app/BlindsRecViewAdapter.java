package com.helio.app;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.RelativeLayout;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.cardview.widget.CardView;
import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;

public class BlindsRecViewAdapter extends RecyclerView.Adapter<BlindsRecViewAdapter.ViewHolder> {

    private ArrayList<Blinds> blinds = new ArrayList<>();

    private Context context;

    public BlindsRecViewAdapter(Context context){
this.context = context;
    }


    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.blinds_list_item,parent,false);
        ViewHolder holder = new ViewHolder(view);
        return holder;
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        holder.txtName.setText(blinds.get(position).getName());
        holder.parent.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(context,blinds.get(position).getName() + " Selected", Toast.LENGTH_SHORT).show();
            }
        });


    }

    @Override
    public int getItemCount() {
        return blinds.size();
    }

    public void setBlinds(ArrayList<Blinds> blinds) {
        this.blinds = blinds;
        notifyDataSetChanged();
    }

    public class ViewHolder extends RecyclerView.ViewHolder{

            private TextView txtName;
            private CardView parent;
            public ViewHolder(@NonNull View itemView){
                super(itemView);
                txtName = itemView.findViewById(R.id.txtName);
                parent = itemView.findViewById(R.id.parent);
            }
        }

}
