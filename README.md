---------------------------------------- Kubeadm Installation ------------------------------------------ 

-------------------------------------- Both Master & Worker Node ---------------------------------------
  sudo su
  apt update -y
  apt install docker.io -y
  
  systemctl start docker
  systemctl enable docker
  
  sudo apt-get update
  # apt-transport-https may be a dummy package; if so, you can skip that package
  sudo apt-get install -y apt-transport-https ca-certificates curl gpg
  
  curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.29/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
  
  echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.29/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
  
  sudo apt-get update
  sudo apt-get install -y kubelet kubeadm kubectl
  sudo apt-mark hold kubelet kubeadm kubectl
  
  sudo systemctl enable --now kubelet

--------------------------------------------- Master Node -------------------------------------------------- 
sudo su
kubeadm init

# To start using your cluster, you need to run the following as a regular user:
  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

# Alternatively, if you are the root user, you can run:
  export KUBECONFIG=/etc/kubernetes/admin.conf
  
kubectl apply -f https://github.com/weaveworks/weave/releases/download/v2.8.1/weave-daemonset-k8s.yaml

kubeadm token create --print-join-command



------------------------------------------- Worker Node ------------------------------------------------ 
sudo su
kubeadm reset pre-flight checks
-----> Paste the Join command on worker node and append `--v=5` at end
