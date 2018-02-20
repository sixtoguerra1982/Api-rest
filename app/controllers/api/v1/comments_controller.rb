module Api
  module V1
    class CommentsController < ApplicationController
      def index
        comments = Comment.order('created_at DESC');
        render json: {status: 'SUCCESS', message:'Loaded Comments', data:comments},status: :ok
      end

      def show
        comment = Comment.find(params[:id])
        render json: {status: 'SUCCESS', message:'Loaded Comment', data:comment},status: :ok
      end

      def create
        comment = Comment.new(comment_params)
        if comment.save
          render json: {status: 'SUCCESS', message:'Saved Comment', data:comment},status: :ok
        else
          render json: {status: 'ERROR', message:'Comment not saved', data:comment.errors},status: :unprocessable_entity
        end
      end

      private

      def comment_params
        params.permit(:feed_id, :user_id, :content)
      end

    end
  end
end
