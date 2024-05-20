from flask import Flask
import os, subprocess
import serial
import sqlite3
import datetime
import uuid
import json
import pyttsx3
import queue
import threading

class speakerThread(threading.Thread):

    def __init__(self, queue):

        threading.Thread.__init__(self)
        self.queue = queue
        self.dameon = True
        self.start()

    def run(self):

        self.engine = pyttsx3.init()

        self.engine.startLoop(False)
        self.engineRunning = True

        while self.engineRunning:
            if self.queue.empty():
                self.engine.iterate()
            else:
                words = self.queue.get()
                if words == 'terminate':
                    self.engineRunning = False
                else:
                    self.engine.say(words)

        self.engine.endLoop()

app = Flask(__name__)

theQueue = queue.Queue()
theEngine = speakerThread(theQueue)

@app.route('/')
def healthCheck():
    return "UP"
    
@app.route('/say/<words>')
def sayWords(words):
    print(words)
    theQueue.put(words)

    print("DONE!")    
    return words

