package com.example.ajoudongfe;

import android.content.Context;
import android.graphics.Color;
import android.graphics.drawable.ShapeDrawable;
import android.graphics.drawable.shapes.OvalShape;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.core.content.ContextCompat;
import androidx.recyclerview.widget.RecyclerView;

import com.squareup.picasso.Picasso;

import java.util.ArrayList;
import java.util.List;

import retrofit2.Retrofit;

public class ApplicationResultAdapter extends RecyclerView.Adapter<ApplicationResultAdapter.ItemViewHolder> {
    public static String BASE_URL= "http://10.0.2.2:8000";
    private Context context;
    private Retrofit retrofit;
    private List<ApplicationObject> listData = new ArrayList<>();
    private int uSchoolID;

    public ApplicationResultAdapter(List<ApplicationObject> listData, int uSchoolID) {
        this.listData = listData;
        this.uSchoolID = uSchoolID;
    }


    @NonNull
    @Override
    public ItemViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.application_result_item, parent, false);
        ItemViewHolder itemViewHolder = new ItemViewHolder(view);
        return itemViewHolder;
    }

    @Override
    public void onBindViewHolder(@NonNull ApplicationResultAdapter.ItemViewHolder holder, int position) {
        holder.onBind(listData.get(position));
    }

    @Override
    public int getItemCount() {
        return listData.size();
    }

    class ItemViewHolder extends RecyclerView.ViewHolder {

        private TextView resClubName;
        private ImageView resClubIMG;
        private TextView resStatus;
        private TextView applyDate;

        ItemViewHolder(View itemView) {
            super(itemView);
            resClubIMG = itemView.findViewById(R.id.resClubIMG);
            resClubName = itemView.findViewById(R.id.resClubName);
            resStatus = itemView.findViewById(R.id.resStauts);
            applyDate = itemView.findViewById(R.id.applyDate);
        }

        void onBind(ApplicationObject applicationObject)
        {
            Log.d("ClubName", applicationObject.getClubName());
            resClubName.setText(applicationObject.getClubName());
            setStatus(resStatus, applicationObject.getStatus());
            if(applicationObject.getClubIMG() != null && applicationObject.getClubName().length() > 0) {
                Picasso.get().load(applicationObject.getClubIMG()).into(resClubIMG);
//                uIMG.setBackground(new ShapeDrawable(new OvalShape()));
//                uIMG.setClipToOutline(true);

            }
            else
            {
                resClubIMG.setImageResource(R.drawable.icon);
//                uIMG.setBackground(new ShapeDrawable(new OvalShape()));
//                uIMG.setClipToOutline(true);
            }
            applyDate.setText(applicationObject.getApplyDate());
        }
    }

    private void setStatus(TextView resStatus, int status) {
        int color;
        if(status == 1)
        {
            resStatus.setText("승인");
            resStatus.setTextColor(Color.BLUE);
        }
        else if(status == 0)
        {
            resStatus.setText("심사 중");
            resStatus.setTextColor(Color.GRAY);
        }
        else
        {
            resStatus.setText("거절");
            resStatus.setTextColor(Color.RED);
        }
    }

}