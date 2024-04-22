from googleapiclient.discovery import build
import csv
from tabulate import tabulate as t

def main():
    api_key = "YOUR YOUTUBE API KEY"
    channel_id = input("Channel ID: ")  # Example Channel Id: UCJQJAI7IjbLcpsjWdSzYz0Q
    youtube = build("youtube", "v3", developerKey=api_key)

    data = get_channel_details(youtube, channel_id)
    video_ids = get_video_id_list(youtube, data["Playlist_ID"])
    videos = get_video_list(youtube, video_ids)

    final_result = output(data, videos)
    print(f"Channel Details:\n{final_result[0]},\nList of Videos:\n{final_result[1]}")

def get_channel_details(youtube, channel_id):
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics", id=channel_id
    )
    response = request.execute()

    data = {
        "Channel Name": response["items"][0]["snippet"]["title"],
        "Subscribers": response["items"][0]["statistics"]["subscriberCount"],
        "Total_Videos": response["items"][0]["statistics"]["videoCount"],
        "Playlist_ID": response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"],
    }

    return data

def get_video_id_list(youtube, playlist_id):
    video_ids = []

    request = youtube.playlistItems().list(
        part="snippet,contentDetails",
        playlistId=playlist_id,
        maxResults=50,
    )
    response = request.execute()

    for item in response["items"]:
        video_ids.append(item["contentDetails"]["videoId"])
    next_page_token = response.get("nextPageToken")
    while next_page_token is not None:
        request = youtube.playlistItems().list(
            part="snippet,contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token,
        )
        response = request.execute()

        for item in response["items"]:
            video_ids.append(item["contentDetails"]["videoId"])
        # print (video_ids)
        next_page_token = response.get("nextPageToken")

    return video_ids

def get_video_list(youtube, video_ids):
    videos = []

    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=",".join(video_ids[i : i + 50])
        )
        response = request.execute()

        for video in response["items"]:
            data = {
                "Video_Title": video["snippet"]["title"],
                "Date_of_Release": video["snippet"]["publishedAt"],
                "Views": video["statistics"]["viewCount"],
            }
            videos.append(data)

    return videos

def output(data, videos):
    csv_filename = "output.csv"

    with open(csv_filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        writer.writeheader()
        writer.writerow(data)
        file.write("\n")

        list_fieldnames = videos[0].keys()
        writer = csv.DictWriter(file, fieldnames=list_fieldnames)
        writer.writeheader()
        writer.writerows(videos)

    single_table = t([data], headers="keys", tablefmt="grid")
    list_table = t(videos, headers="keys", tablefmt="grid")

    return single_table, list_table

if __name__ == "__main__":
    main()
