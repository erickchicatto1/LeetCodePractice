    def start(self):
        t_socket = threading.Thread(target=self.socket_thread,daemon=True)
        t_camera = threading.Thread(target=self.camera_thread,daemon=True)
        t_infer = threading.Thread(target=self.inference_thread,daemon=True)
        
        self.threads.extend([t_socket,t_camera,t_infer])
        
        for t in self.threads:
            t.start()
        
        for t in self.threads:
            t.join()
            
