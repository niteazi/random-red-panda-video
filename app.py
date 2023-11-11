from flask import Flask, render_template,request,redirect,url_for
from pytube import Search,YouTube
import random 

app = Flask(__name__, static_folder='static')


def random_video(query):

    s = Search(query)
    s.results  # we need more results
    s.get_next_results()
    total_results = len(s.results)
    random_indices = random.sample(range(total_results), 1) #select random video out of results
    v_id = s.results[random_indices[0]].video_id #get the  id of the random result
    v_url = f"https://www.youtube.com/embed/{v_id}"  # way to integrate v_id together with the url
    #print(v_url)  
    return v_url

@app.route('/download_video', methods=['POST'])
def download():
        vid_url = request.form['vid_url']
        youtubeObject = YouTube(vid_url)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        try:
            youtubeObject.download('C:/Users/nitea/Downloads') #download in downloads
        except:
            print("An error has occurred")
        print("Download is completed successfully")
        return redirect(url_for('index')) #g n mporw n to parw st html



@app.route('/')
def index():
    query = 'cute red pandas'
    v_url = random_video(query)
    return render_template('index.html', v_url=v_url)

if __name__ == '__main__':
    app.run(debug=True)
