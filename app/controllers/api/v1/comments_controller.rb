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
    end
  end
end
