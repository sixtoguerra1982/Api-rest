module Api
  module V1
    class LikesController < ApplicationController
      def index
        likes = Like.order('created_at DESC');
        render json: {status: 'SUCCESS', message:'Loaded Likes', data:likes},status: :ok
      end

      def show
        like = Like.find(params[:id])
        render json: {status: 'SUCCESS', message:'Loaded Like', data:like},status: :ok
      end
    end
  end
end
