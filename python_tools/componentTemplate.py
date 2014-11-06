#coding=utf-8
'''
 componentTemplate.py
 
 Developed by Ocean.Liu<liuhaiyang@playcrab.com>
 Copyright (c) 2014 www.playcrab.com
 
 Changelog:
 2014-11-06 - created
 
'''
import os
import sys
import getopt
from string import Template

channel=''
methods=''

def print_usage():
    print """
Usage:
    python %s <-c channelNae> <-m methods>
    for example:
    python %s -c anzhi -m logout
    python %s -c anzhi -m logout,userCenter
"""%(__file__,__file__,__file__)

def check_param():
    global channel
    global methods

    try:
        opts,args = getopt.getopt(sys.argv[1:], "c:m:")
        if len(opts) <= 0:
            print_usage()
            sys.exit(1)
        for opt in opts:
            if opt[0] == '-c':
                channel = opt[1].capitalize()
            elif opt[0] == '-m':
                methods = opt[1]
    except getopt.GetoptError:
        print_usage()
        sys.exit(1)

def pruduceComponent():
    class_code = Template('''
package com.playcrab.bifrost.components;

import org.json.JSONException;
import org.json.JSONObject;

import android.os.Bundle;

import com.playcrab.bifrost.BifrostAccountComponent;
import com.playcrab.bifrost.BifrostComponentListener;
import com.playcrab.bifrost.utils.BifrostLog;

public class ${className}Component extends BifrostAccountComponent{


    public void init(final JSONObject object) { 
        bf.gameAct.runOnUiThread(new Runnable(){
            @Override
            public void run() {
                  
            }
        }); 
    }

    public void login(final JSONObject jsonMsg) throws JSONException {
        bf.gameAct.runOnUiThread(new Runnable(){
            @Override
            public void run() {
                  
            }
        }); 

    }

    public void chargeDetail(final JSONObject jsonMsg) throws JSONException {
        bf.gameAct.runOnUiThread(new Runnable(){
            @Override
            public void run() {
                  
            }
        }); 
    }

 ''')

    method_code = Template('''
    public void ${methodName}(final JSONObject json) {
            bf.gameAct.runOnUiThread(new Runnable(){
                @Override
                public void run() {
                  
                }
            }); 
    }
''')
    end_str= '''
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    public void onStart() {
        super.onStart();
    }

    public void onRestart() {
        super.onRestart();
    }

    public void onResume() {
        super.onResume();
    }

    public void onPause() {
        super.onPause();
    }

    public void onStop() {
        super.onStop();
    }

    public void onDestroy() {
        super.onDestroy();
    }

    public void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
    }

}
'''
    code = class_code.substitute(className=channel)

    for method in methods.split(","):
        method_str = method_code.substitute(methodName=method)
        code = code + method_str

    code = code + end_str
    saveFile(code, channel+"Component.java")

def saveFile(code, path):
    print path
    try:
        f = open(path, 'w')
        f.write(code)
    finally:
        f.close()

def main():
    check_param()
    pruduceComponent()


if __name__ == "__main__":
    main()
