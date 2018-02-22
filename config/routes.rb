Rails.application.routes.draw do

  root 'home#index'

  namespace 'api' do
    namespace 'v1' do
      resources :feeds, only: [:index, :show]
      resources :likes, only: [:index, :show, :create]
      resources :comments, only: [:index, :show, :create]
    end
  end

  get 'likes/index'
  get 'comments/index'
  get 'feeds/index'

  resources :feeds, only: [:create]

end
