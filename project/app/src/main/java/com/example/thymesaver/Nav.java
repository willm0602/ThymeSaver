package com.example.thymesaver;

import android.content.Context;
import android.util.AttributeSet;

import androidx.annotation.NonNull;
import androidx.constraintlayout.widget.ConstraintLayout;

public class Nav  extends ConstraintLayout {
    public Nav(@NonNull Context context, AttributeSet attributes) {
        super(context,attributes);
        init(context,attributes);
    }

    private void init(Context context, AttributeSet attrs) {
        inflate(context, R.layout.nav, this);

        System.out.println("Test!");
    }


}
