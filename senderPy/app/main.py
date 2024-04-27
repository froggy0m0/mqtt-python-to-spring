import time
from datetime import datetime
import mqtt_client

def main():
    client = mqtt_client.setup_mqtt_client()

    # MQTT 클라이언트를 시작합니다. 모든 메시지 처리는 background thread에서 수행됩니다.
    client.loop_start()

    try:
        while True:
            message = "Hello, MQTT! " + datetime.now().isoformat()
            mqtt_client.publish_message(client, "hello/mqtt", message)
            print(f"Published: {message}")
            time.sleep(1)  # 메시지 전송 간의 딜레이
    except KeyboardInterrupt:
        print("Interrupted by user, shutting down.")
    finally:
        client.loop_stop()  # background 네트워크 루프를 멈춥니다.
        client.disconnect()  # 클라이언트 연결을 종료합니다.
        print("MQTT client disconnected.")

if __name__ == "__main__":
    main()
