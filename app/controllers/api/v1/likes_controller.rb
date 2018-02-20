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

      def create
        like = Like.new(like_params)
        if like.save
          render json: {status: 'SUCCESS', message:'Saved Like', data:like},status: :ok
        else
          render json: {status: 'ERROR', message:'Like not saved', data:like.errors},status: :unprocessable_entity
        end
      end

      private

      def like_params
        params.permit(:feed_id, :user_id, :like)
      end

    end
  end
end
